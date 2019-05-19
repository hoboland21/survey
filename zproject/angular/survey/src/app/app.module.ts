import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SurveyComponent } from './survey/survey/survey.component';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { NotfoundComponent } from './system/notfound/notfound.component';
import { SurveyCheckComponent } from './survey/survey-check/survey-check.component';
import { SurveyMasterComponent } from './survey/survey-master/survey-master.component';
import { SurveyStepZeroComponent }  from './survey/survey-master/survey-step-zero.component';
import { SurveyStepOneComponent }  from './survey/survey-master/survey-step-one.component';
import { AppConstants } from './system/app.constants';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    SurveyComponent,
    NotfoundComponent,
    SurveyCheckComponent,
    SurveyMasterComponent,
    SurveyStepZeroComponent,
    SurveyStepOneComponent
  ],

  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [AppConstants],
  bootstrap: [AppComponent]
})
export class AppModule { }
