---
date:
    created: 2025-05-01
tags:
  - Programming
---
This is my flutter note.
<!-- more -->

# 0. SetUp

## 1. Flutter sdk

1. config environment var in PATH: `<Flutter_Directory>/bin`

   

2. After installing flutter, execute: `flutter doctor` to verify





## 2. Android Studio

阶段一: 创建模拟器设备

1. Create device:

   

2. Choose system:

   

3. Use graphic card:

   

4. advanced setting里要设置cold boot

阶段二: 安装插件

1. market搜索flutter

阶段三: 在emulator里打开项目

1. 选择项目:

   

2. 第一次打开时，会让你配置dart路径

   

3. 

   

4. 再启动



# 1. Concept Overview

Mobile UI Layout(widget tree)

+ root widget
  + App bar widget
  + Container widget





Other widgets:

+ text widget
+ button widget
+ row widget
+ column widget
+ Image Widget

# 2. Dart

## 1. Data type

Dart is a statically language, once we assign the type, we cannot assign a value of different type to it but u can change the type through keyword `dynamic`, basic types:

+ `String`

+ `int`

+ `bool`

+ `List`

+ `class`

  ```dart
  List name = ["chun-li", "yoshi", "mario"];
  
  name.add("luigi");
  names.remove("yoshi")
  // Pure List can add different data type, so we can specify the content type by following lines
  names.add(30)
      
  List<Sting> stringList = []
  ```

  



## 2. Demo code

+ Create a class object:

  ```dart
  class User {
      String username = "hi";
      int age = 5;
      
      User(String s, int a){
          this.username = s;
          this.age = a;
      }
      
      void login(){
          print("logged in");
      }
  }
  
  void main(){
      User u = User("jack", 2);
      // the apprpriate way to call constructor is: User u = User(s: "jack", a: 2);
      print(u.username);
      u.login()
  }
  ```

+ Inheritance:

  ```dart
  class SuperUser extends User {
      // calls the constructor from the super class
      SuperUser(String username, int age): super(username, age);
      
      void publish(){
          print("published")
      }
  }
  
  void main(){
      SuperUser su = SuperUser("jack", 2);
      su.publish();
      su.login();
  }
  ```

  

+ function:

  ```dart
  String greeting(){
      return "hello";
  }
  ```

  

+ use of `dynamic`:

  ```dart
  void main(){
      dynamic name = 'chun-li';
      name = 30;
      print(name);
  }
  ```

  

+ for loop:

  ```dart
  void main(){
      for(int i = 0; i < 5; i++){
          print('hello ${i + 1}')
      }
  }
  ```

  

## 3. Widget Concepts

+ Stateless Widget vs Stateful widget:
  + Stateless: the state of the widget cannot change over time
  + Stateful: the state of the widget can change over time



Widget hierachy:

> MaterialApp
>
> > Scaffold
> >
> > > AppBar
> > >
> > > Body
> > >
> > > > Container
> > > >
> > > > Padding

+ Container widget: 

  >  It's a box. When it has no child, it will occupy the whole parent widget. When it has a child, it will occupy the same size as its child(such as text widget if its child is Text widget)
  >
  > + padding(property): example below
  >
  >   ```dart
  >   Container(
  >       padding: EdgeInsets.symmetric(horizontal: 30.0, vertical: 10.0)
  >       // padding: EdgeInsets.fromLTRB(10.0, 20.0, 30.0, 40.0)
  >   )
  >   ```
  >
  >   

+ Scaffold
+ Padding
+ AppBar
+ MaterialApp
+ StatelessWidget
+ StatefulWidget
+ Row
+ Column

method of Widget class:

+ build:(This function helps hot reload)

  ```dart
  class Home extends StatelessWidget{
      @Override
      Widget build(BuildContext context){}
  }
  ```

  

Property of Widget class:

+ child: `<Widget>` type



## 4. Stateful Widget

Demo:

```dart
// step2: create the factory class for that widget
class Test extends StatefulWidget {
    @override
    _TestState createState() => _TestState();
}

// step1: create the stateful widget class and let it extends State
class _TestState extends State<Test> {
    int state1;
    String state2;
    // .. any other states, and then use setState((){...}) to change state inside 
    // build function
    @override
    Widget build(BuildContext context){
        return Container();
        // return how you define the Test Widget
    }
}
```



## 5. Define Route rules

Route demo:

Suppose the file folder is as following:

> world_time
>
> > android
>
> > ios
>
> > lib
> >
> > > pages
> > >
> > > > Home.dart
> > > >
> > > > ChooseLocation.dart
> > > >
> > > > Loading.dart
> > >
> > > main.dart

how to define routes in main.dart:

```dart
import "package:flutter/material.dart";
import "package:world_time/pages/home.dart";
import "package:world_time/pages/Loading.dart";
import "package:world_time/pages/ChooseLocation.dart";

void main() => runApp(MaterialApp(
    home: Home();
    routes: {
        "/": (context) => Loading(),
        "/home": (context) => Home(),
        "/location": (context) => ChooseLocation()
    }
))
```



## 6. Navigate route button

use the function`Navigator.pushNamed`

```dart
class _HomeState extends State<Home> {
    @override
    Widget build(BuildContext context){
        return Scaffold(
            body: SafeArea(
                child: Column(
                    children: <Widget>[
                        FlatButton.icon(
                            onPressed: (){
                                Navigator.pushNamed(context, "/location")
                            },
                            icon: Icon(Icons.edit_location),
                            label: Text("edit location")
                        )
                    ]
                )
            )
        )
    }
}
```



## 7. The behind routing mechanism

https://www.youtube.com/watch?v=WG5tJIAq5b0&list=PL4cUxeGkcC9jLYyp2Aoh6hcWuxFDX6PBJ&index=23



## 8. Widget Lifecycle

Stateless:

+ State does not change over time
+ build function only runs once

Stateful:

+ State can change over time
+ setState() triggers the build function



**Stateful:**

initState -> Build -> setState -> Build -> dispose



## 9. Async code

https://www.jianshu.com/p/cec4e117fce4

demo:

```dart
void getData() async {
    String username = await Future.delayed(Duration(seconds: 3), (){
        return "hi";
    });
    String bio = await Future.delayed(Duration(seconds: 2), (){
        return "hello";
    });
    print('${username} - ${bio}');
}
```



# 3. Config

+ ./publicspec.yaml

