const waveCanvas = document.getElementById("waveCanvas");
const waveCtx = waveCanvas.getContext("2d");

const fftCanvas = document.getElementById("fftCanvas");
const fftCtx = fftCanvas.getContext("2d");

// connect WebSocket
const ws = new WebSocket(`ws://${window.location.host}/ws`);
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const volume = data.volume;
    const fft = data.fft;

    // draw simple volume bar
    waveCtx.clearRect(0, 0, waveCanvas.width, waveCanvas.height);
    waveCtx.fillStyle = "red";
    waveCtx.fillRect(0, waveCanvas.height - volume / 1000, 50, volume / 1000);

    // draw FFT
    fftCtx.clearRect(0, 0, fftCanvas.width, fftCanvas.height);
    fft.forEach((v, i) => {
        fftCtx.fillStyle = "blue";
        fftCtx.fillRect(i * 4, fftCanvas.height - v / 1000, 3, v / 1000);
    });
};

// capture microphone
navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start(100); // chunk every 100ms
    mediaRecorder.ondataavailable = e => {
        const reader = new FileReader();
        reader.onloadend = () => ws.send(reader.result);
        reader.readAsDataURL(e.data);
    };
});