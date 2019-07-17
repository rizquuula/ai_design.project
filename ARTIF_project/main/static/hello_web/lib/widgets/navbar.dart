import 'package:flutter_web/material.dart';
import 'package:hello_web/utils/responsiveLayout.dart';

class NavBar extends StatelessWidget{
final navLinks = ["Home","Products","About"];

List<Widget> navItem(){
  return navLinks.map((text){
    return Padding(
      padding: EdgeInsets.only(left: 18),
      child: Text(text,)
    );
  }).toList();
}

  @override 
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.symmetric(
        horizontal: 45,
      vertical: 38),
    child: Row(
         mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: <Widget>[
        Row(
        children: <Widget>[
          Container(
            width:60 ,
            height: 60,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(18),
              gradient:LinearGradient(
                colors:[
                  Colors.blue[900],Colors.blue[300]
                ],
                begin: Alignment.bottomRight,end: Alignment.topLeft)),
                child: Center(child: 
                Text("A",
                style: TextStyle(fontSize: 30,
                color: Colors.white)),
                ),
                ),
                SizedBox(
                  width: 16,
                ),
                Text(
                  "Artif Studio",
                  style: TextStyle(
                    fontSize: 26))
        ],
        ),
        if (!ResponsiveLayout.isSmallScreen(context))
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: <Widget>[...navItem()],
        )
      ],
    ),
    );
  }
}