import 'package:flutter/material.dart';
import '/value.dart';

class CustomForm extends StatelessWidget {
  final text_Control_CAM = TextEditingController();
  final text_Control_GPS = TextEditingController();

  CustomForm();

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text("Drone CAM URL"),
          SizedBox(height: small_gap),
          TextField(
            controller: text_Control_CAM,
          )
        ]),
        SizedBox(height: large_gap),
        Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text("Drone GPS URL"),
          SizedBox(height: small_gap),
          TextField(
            controller: text_Control_GPS,
          )
        ]),
        SizedBox(height: large_gap),
        TextButton(
          style: TextButton.styleFrom(
            backgroundColor: Colors.pink,
            foregroundColor: Colors.white,),
          onPressed: () {
            cam_url = text_Control_CAM.text;
            gps_url = text_Control_GPS.text;
            Navigator.pushNamed(context, "/home");
          },
          child: Text("Login"),
        ),
      ],
    );
  }
}