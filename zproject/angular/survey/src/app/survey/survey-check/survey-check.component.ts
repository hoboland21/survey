import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { IAnswer } from '../answer';

@Component({
  selector: 'app-survey-check',
  templateUrl: './survey-check.component.html',
  styleUrls: ['./survey-check.component.css']
})
export class SurveyCheckComponent implements OnInit {
  isSubmitted = false;
  answer:number ;
  @Output() marked = new EventEmitter<number>();
  @Input() question :string;
  constructor(
    private formBuilder:FormBuilder,


  ) { }



  answerForm = this.formBuilder.group({
    check:["",[Validators.required]]
  }) 
  //get myForm() {
  //  return this.answerForm.get('check');
  
  
 // }
  onSubmit() {
    this.isSubmitted = true;
    if(!this.answerForm.valid) {
      return false;
    } else {
      
      this.marked.emit(this.answerForm.value["check"]);
      this.answerForm.controls['check'].reset();

    }
  }

  ngOnInit() {
  }

}
