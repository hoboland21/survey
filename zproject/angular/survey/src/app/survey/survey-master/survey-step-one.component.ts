import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ICourse } from '../course';
import { CourseService } from '../course.service';
import { AnswerService } from '../answer.service';


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
  <hr>
  <app-survey-answer [studentId]="studentId"></app-survey-answer>
  <hr>
  <button class="btn btn-primary mt-3" type="submit" [disabled]="!courseForm.valid">
    Next</button>
</form>

`
})

export class SurveyStepOneComponent implements OnInit {
  courseList = new Set();
  errorMessage = "";
  offset = 0;
  @Input() courses : ICourse[];
  @Input() studentId:number;
  @Output() courseOut:EventEmitter<ICourse> = new EventEmitter();
  
  constructor(
    private formBuilder:FormBuilder,
    private answerService:AnswerService,
    private courseService: CourseService
  ) { }

  courseForm = this.formBuilder.group({
    course:["",[Validators.required]],
  }) 
  
  
  ngOnInit() {
 }

  continue() {
    this.answerService.getAnswer(this.studentId).subscribe(
      data => {
        data.forEach(answer => this.courseList.add(answer.course) );
        this.offset= this.courseForm.value["course"]
        if (!this.courseList.has(this.courses[this.offset].id)) {
          this.courseOut.emit(this.courses[this.offset]);

        }
          
      
      })


  }
  
}