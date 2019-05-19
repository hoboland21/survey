import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { IStudent } from '../student';
import { ICourse } from '../course';
import { SurveyService } from '../survey.service';
import { ISurvey } from '../survey';
import { AnswerService } from '../answer.service';
import { AppConstants } from '../../system/app.constants';
import { CourseService } from '../course.service';

@Component({
  selector: 'app-survey-master',
  templateUrl: './survey-master.component.html',
  styleUrls: ['./survey-master.component.css']
})
export class SurveyMasterComponent implements OnInit {
  surveyId:number;
  studentName:string;
  courses:ICourse[];
  course:ICourse;
  student:IStudent;
  survey:ISurvey;
  
  surveyInit = 0;
  errorMessage = "";

  surveyStep = 0;
  
  constructor(
    private formBuilder:FormBuilder,
    private surveyService: SurveyService,
    private answerService: AnswerService, 
    private courseService: CourseService,
    private appconst: AppConstants,
    private _router:  Router,
    private _route:   ActivatedRoute,
  ) { }
  
  GRADELEVEL = this.appconst.GRADELEVEL;

   
  //====================================
  ngOnInit() {
    this.surveyId = Number(this._route.snapshot.paramMap.get('id'));
    this.studentName = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
    this.surveyService.getSurvey(this.surveyId).subscribe(
      survey => {
        this.survey = survey;
      },
      error => this.errorMessage = <any>error
    );
    this.courseService.getCourseList().subscribe(
      courses => {
        this.courses = courses
      },
      error => this.errorMessage = <any>error
    );

    this.student = {
      name:this.studentName,
      survey: this.surveyId,
      grade_level:"",
      test_code:"",
      created:new Date()
    }
  }

  //====================================
  register_student_header(newStudent:IStudent) {
    this.answerService.addStudent(newStudent).subscribe(
      data => {  
        newStudent.id =  data.id;
        this.student = newStudent;
        this.surveyStep += 1;
      } ,
      error => {
        this.errorMessage= "Failed to create student Component";
      }
    )
    console.log(this.student);
  }
  //====================================
  register_course(course:ICourse) {
    this.course = course;
    this.surveyStep += 1;
  }
  //====================================
  surveyOut() {
    this.surveyStep -= 1;
  }
}
