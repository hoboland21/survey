import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-survey-check',
  templateUrl: './survey-check.component.html',
  styleUrls: ['./survey-check.component.css']
})
export class SurveyCheckComponent implements OnInit {
  isSubmitted = false;

  constructor(
    private formBuilder:FormBuilder,


  ) { }

  answerForm = this.formBuilder.group({
    check:["",[Validators.required]]
  }) 
  get myForm() {
    return this.answerForm.get('check');
  
  
  }
  onSubmit() {
    this.isSubmitted = true;
    if(!this.answerForm.valid) {
      return false;
    } else {
      this.answerForm.controls['check'].reset();

    }
  }

  ngOnInit() {
  }

}
