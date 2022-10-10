import 'package:flutter/material.dart';
import '/components/custom_form.dart';
import '/value.dart';

class LoginPage extends StatelessWidget {

  LoginPage();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ListView(
          children: [
            const SizedBox(height: xlarge_gap),
            const Text('Enter URL', style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold),),
            const SizedBox(height: large_gap),
            CustomForm(),
          ],
        ),
      ),
    );
  }
}