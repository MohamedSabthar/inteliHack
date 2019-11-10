import { AngularFirestore } from '@angular/fire/firestore';
import { Dates } from './../currentsemester/dates';
import { AngularFireAuth } from '@angular/fire/auth';
import { RouterModule } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { User } from 'firebase';
import { Observable } from 'rxjs';
import * as firebase from 'firebase';

@Component({
  selector: 'app-attendance',
  templateUrl: './attendance.component.html',
  styleUrls: ['./attendance.component.css']
})
export class AttendanceComponent implements OnInit {
  
  user: firebase.User;
  index;
  countT = 0;
  countA = 0;
  per:number;
  constructor(private router: RouterModule, public authService: AuthService, private afAuth: AngularFireAuth, private db:AngularFirestore) {
   afAuth.authState.subscribe(user => this.user = user);
   }
   

  ngOnInit() {
    this.db.collection('Register',ref => ref.where('id', '==', '2017cs004')).valueChanges().subscribe(val => {
      console.log(val);
      this.index = val;
      for (let dd of val) {
        this.countA++;
      }
    })

    this.db.collection('Register').valueChanges().subscribe(val => {
      
      for (let dd of val) {
        this.countT++;
      }
    })
  }
  
}
