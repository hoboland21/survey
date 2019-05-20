import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { AppConstants } from '../../system/app.constants';
import { IStudent } from '../student';


@Component({
  selector: 'app-survey-zero',
  template: `
   <form [formGroup]="studentForm" (ngSubmit)="continue()" novalidate>
<input type="text" id='test_code' class="form-control" 
  formControlName="test_code" name="test_code">

<label for="test_code">Test Code</label>

<select formControlName="grade_level" name="grade_level"
  id="grade_level" class="form-control">
  <option disabled selected value> -- select -- </option> 
  <option *ngFor="let gl of GRADELEVEL" [value]='gl'>{{ gl }}</option>
  <option></option>
</select>
<label for="grade_level">Grade Level</label>
<button class="mt-3 btn btn-primary" type="submit" [disabled]="!studentForm.valid">
  Begin Survey</button>
</form>
  `
})

export class SurveyStepZeroComponent implements OnInit {
  test_code:number;
  grade_level:string;
  errorMessage = "";

  @Input() student:IStudent
  @Output() studentOut:EventEmitter<IStudent> = new EventEmitter();
  

  constructor(
    private formBuilder:FormBuilder,
    private appconst: AppConstants,
  ) { }


  studentForm = this.formBuilder.group({
    grade_level:["",[Validators.required]],
    test_code:["",[Validators.required]]
  }) 
  
  GRADELEVEL = this.appconst.GRADELEVEL;

  ngOnInit() {
  }

  continue() {
    this.student.test_code = this.studentForm.value["test_code"];
    this.student.grade_level = this.studentForm.value["grade_level"];
    this.studentOut.emit(this.student);

  }
  
}