import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html'
})
export class MainComponent {
  processing: boolean = false;
  
  textControl: FormControl = new FormControl(`Рассказ “Ночь перед Рождеством” входит в цикл “Вечера на хуторе близ Диканьки”. В этом раннем произведении Н. В. Гоголь показал, что мастерски владеет словом и является прекрасным писателем-сатириком. На сайте представлены сочинения по повести “Ночь  перед Рождеством”.
На создание этого произведения повлияло детство писателя, которое он провел в украинской деревни и впитал в себя и очень полюбил местный фольклор.
В основе сюжета – жизнь украинской деревни в канун Рождества. Гоголь мастерски описывает украинскую зимнюю природу, а также вносит мистическую ноту в сюжет произведения. Главным героем является молодой кузнец Вакула.`);
  picthControl: FormControl = new FormControl(1); // 0 to 2
  rateControl: FormControl = new FormControl(1); // 0.1 to 1
  voiceControl: FormControl = new FormControl(0);
  volumeControl: FormControl = new FormControl(0.5); // 0 to 1

  readonly LANG: string = "ru-RU";
  readonly SYNTH: SpeechSynthesis;
  readonly UTTER: SpeechSynthesisUtterance;

  constructor() {
    this.SYNTH = window.speechSynthesis;
    this.UTTER = new SpeechSynthesisUtterance();
    this.UTTER.lang = this.LANG;
    this.setUtterProperties();
  }

  async TextToVoice(): Promise<void> {
    if (this.SYNTH.speaking) {
      this.SYNTH.cancel();
    }
    this.setVoice();
    this.UTTER.text = this.textControl.value;
    this.SYNTH.speak(this.UTTER);
  }

  setUtterProperties(): void {
    this.stop();
    this.UTTER.pitch = this.picthControl.value;
    this.UTTER.rate = this.rateControl.value;
    this.UTTER.volume = this.volumeControl.value;
  }

  private setVoice(): void {
    this.UTTER.voice = this.SYNTH.getVoices().filter((voice) => voice.lang == "ru-RU")[this.voiceControl.value];
  }

  stop(): void {
    if (this.SYNTH.speaking) {
      this.SYNTH.cancel();
    }
  }

  pause(): void {
    if (this.SYNTH.speaking) {
      this.SYNTH.pause();
    }
  }

  resume(): void {
    if (this.SYNTH.paused) {
      this.SYNTH.resume();
    }
  }
}
