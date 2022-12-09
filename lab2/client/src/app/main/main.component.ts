import { Component } from '@angular/core';
import { AnalyzeService } from '../analyze.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html'
})
export class MainComponent {
  processing: boolean = false;
  result: string = "";

  constructor(
    private analyze: AnalyzeService
  ) { }

  async AnalyzeFiles(): Promise<void> {
    this.processing = true;
    const fileInput = <HTMLInputElement>document.querySelector("#files");
    const fileList = fileInput.files;

    if (!fileList) {
      this.processing = false;
      return;
    }

    await this.analyze.File(fileList).then((result) => {
      this.result += "\n" + result;
      this.processing = false;
    });
  }

  ClearLog(): void {
    this.result = "";
  }
}
