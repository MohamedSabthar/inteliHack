import { DateService } from './date.service';
import { AngularFireAuth } from '@angular/fire/auth';
import { environment } from './../environments/environment';
import { AngularFireDatabaseModule } from 'angularfire2/database';
import { AngularFirestore } from '@angular/fire/firestore';
import { AngularFireModule } from '@angular/fire';
import { AngularFireDatabase } from 'angularfire2/database';
import { RouterModule,Routes } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToastrModule } from 'ngx-toastr';
import { ManageUserService } from './manage-user.service';
import { ManageHallsService } from './manage-halls.service';
import { AuthService } from './auth.service';
import { ChartsModule } from 'ng2-charts';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { SigninComponent } from './signin/signin.component';
import { HomeComponent } from './home/home.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { AttendanceComponent } from './attendance/attendance.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ManageUsersComponent } from './manage-users/manage-users.component';
import { DashboardAdminComponent } from './dashboard-admin/dashboard-admin.component';
import { CurrentsemesterComponent } from './currentsemester/currentsemester.component';




@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    SigninComponent,
    HomeComponent,
    SignUpComponent,
    AttendanceComponent,    
    ManageUsersComponent,
    DashboardAdminComponent,
    CurrentsemesterComponent
 
  ],
  imports: [
    AngularFireModule.initializeApp(environment.firebase),
    RouterModule.forRoot([
      {path: '',component: HomeComponent},
      { path: 'Home', component: HomeComponent },
      { path: 'SignIn', component: SigninComponent },
      { path: 'SignUp', component: SignUpComponent },
      { path: 'Attendance', component: AttendanceComponent },
      { path: 'ManageUsers', component: ManageUsersComponent },
      { path: 'currentsemester', component: CurrentsemesterComponent },
      { path: 'Dashboard', component: DashboardAdminComponent}
    ]),
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    NgbModule,
    ChartsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    ToastrModule.forRoot({ timeOut: 6000, positionClass: 'toast-top-center', preventDuplicates: false }),
  ],
  providers: [AngularFirestore,ManageUserService,ManageHallsService,AngularFireDatabase, AuthService,AngularFireAuth,DateService],
  bootstrap: [AppComponent]
})
export class AppModule { }
