window.recognizeVoice = () => new Promise((resolve) => {

  const recognizer = new webkitSpeechRecognition();

  recognizer.interimResults = true;

  recognizer.lang = 'ru-Ru';

  recognizer.onresult = (event) => {
    const result = event.results[event.resultIndex];
    if (result.isFinal) {
      resolve(result[0].transcript);
    }
  };

  recognizer.start();
});