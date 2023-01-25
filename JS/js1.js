// //numbers
// let l = 4.5;
// let w = 5.6;
// //strings
// let s ="Hello"
// let color = "pink"
// //Booleans
// let x= true
// let y = false
// //Object
// const emp = {fname : "Akshit", lname : "Khamesra"}
// //arrays
// cars = ["BMW", "Suzuki", "Audi"]
// //Date
// const d = new Date('2023-01-23')
// //
// string1 = 10
// string2 = 20
// let str = "Apple, Banana, Kiwi";
// let part = str.slice(-12, 35);
// //

// string1 = "Hello World"
// string2 = "! This is me."
// const arr1 = ['a', 'b', 'c']
// document.getElementById('demo2').innerHTML = arr1;
// const arr1 = [1,2,3,4,5]
// for(let key in arr1){
//     console.log(arr1[key])
// }
// const arr1 = [1,2,3,4,5]
// for(let key of arr1){
//     console.log(key)
// }

// class Emp{
//     static company = "Bajaj Markets";
//     constructor(eid, ename,esal){
//         this.eid = eid;
//         this.ename = ename;
//         this.esal = esal;
//     }
//     set emp_id(eid){this.eid = eid;}
//     set emp_name(ename){this.ename = ename;}
//     set emp_sal(esal){this.esal = esal;}
//     get emp_id(){return this.eid;}
//     get emp_name(){return this.ename;}
//     get emp_sal(){return this.esal;}
//     disp(){
//         console.log(this.eid,this.ename,this.esal);
//     }
//     static get_company(){ return Emp.company;}
// }
// let e1 = new Emp("EO1","Akshit",35000);
// console.log(e1.disp(),Emp.get_company())
// console.log(e1.emp_id,e1.ename,e1.esal)
// e1.eid = "EO2"
// e1.ename = "Aryamaan"
// e1.esal = 50000;
// Emp.company = "Bajaj Finserv"
// console.log(e1.disp(), Emp.get_company())

// class Meetup{
//     constructor(organizer){
//         this.organizer = organizer;
//     }
// }

// class Teachmeet extends Meetup{
//     constructor(organizer,techtopic){
//         super(organizer);
//         this.teachtopics = techtopic;
//     }
// }

// let js = new Teachmeet("Unext", "Microservices");
// console.log(js.organizer, "-", js.teachtopics);

// BLOCK SCOPE
// m = 4;
// n = 2;
// if(m>n){
//     var p =4; //accessiblev
// }
// console.log(p); 

// if(m>n){
//     let g = 10; // not accessible
// }
// console.log(g);

//FUNCTION SCOPE
// function f1(){let v1 = 10}
// function f2(){var v2 = 20}
// function f3(){const v3 = 30}
// console.log(v1,v2,v3) // not accessible

//GLOBAL SCOPE
// var v5 = 40;
// let v6 = 50;
// const v7 = 60;
// function check(){
//     v5 = 66;
//     v6 = 77;
// }
// check()
// console.log(v5,v6,v7);