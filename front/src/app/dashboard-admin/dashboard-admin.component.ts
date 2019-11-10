import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard-admin',
  templateUrl: './dashboard-admin.component.html',
  styleUrls: ['./dashboard-admin.component.css']
})
export class DashboardAdminComponent implements OnInit {

  constructor() { }

  public barChartOptions = {
    scaleShowVerticalLines: false,
    responsive: true
  };

  public barChartLabels = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013'];
  public barChartType = 'line';
  public barChartLegend = true;

  public barChartData = [
    { data: [56, 43, 23, 56, 67, 66, 34, 56], label: 'Series A' },
    { data: [23, 45, 23, 45, 33, 89, 54, 23], label: 'Series B' }
  ];
  ngOnInit() {
  }

}
