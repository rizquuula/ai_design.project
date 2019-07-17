import 'package:flutter_web/material.dart';
import 'package:hello_web/widgets/navbar.dart';

void main() => runApp(MaterialApp(
  title: 'Selamat Datang',
  debugShowCheckedModeBanner: false,
  theme: ThemeData(
    primarySwatch: Colors.blue,
  ),
  home: HomePage(),
    ));
  
  class HomePage extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
      return Container(
        decoration: BoxDecoration( color: Colors.white
          ),
          child: Scaffold(
            backgroundColor: Colors.transparent,
            body: SingleChildScrollView(
              child: Column(
                children: <Widget>[NavBar()],
              ),),
          ),
      );
    }
  }