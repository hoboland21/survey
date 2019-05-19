import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ICourse } from '../course';
import { CourseService } from '../course.service';


@Component({
  selector: 'app-survey-one',
  template: `

<h4>Please select a teacher, class and section</h4>

<form [formGroup]="courseForm" (ngSubmit)="continue()">
  <select formControlName="course" name="course"
    id="course" class="form-control">
    <option disabled selected value > -- select -- </option> 
    <option *ngFor="let cr of courses; let i = index" [value]='i'>
      {{ cr.instructor }} - {{ cr.title }} -- {{ cr.section }}</option>
    <option></option>
  </select>

  <button class="btn btn" type="submit" [disabled]="!courseForm.valid">
    Next</button>
</form>

`
})

export class SurveyStepOneComponent implements OnInit {
  
  errorMessage = "";
  offset = 0;
  @Input() courses : ICourse[];
  @Output() courseOut:EventEmitter<ICourse> = new EventEmitter();
  
  constructor(
    private formBuilder:FormBuilder
  ) { }

  courseForm = this.formBuilder.group({
    course:["",[Validators.required]],
  }) 
  
  
  ngOnInit() {
  }

  continue() {
    this.offset= this.courseForm.value["course"]
    this.courseOut.emit(this.courses[this.offset]);

  }
  
}