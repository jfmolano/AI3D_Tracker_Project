using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

public class Score : MonoBehaviour {

	public static int puntos;
	public static int final_puntos;
	public static string texto;
	public static string timeLeft_text;
	public static float timeLeft;
	public static bool end;

	void Start () {
		timeLeft = 10000f;
		end = false;
	}

    void OnGUI()
 	{
 		timeLeft -= 1;
 		if (timeLeft <= 0){
 			end = true;
 		}
	 	GUI.contentColor = Color.black;
 		if(!end){
	 		timeLeft_text = "T: " + timeLeft;
	 		texto = "Score: " + puntos;
	 		texto = texto + "\n" + timeLeft_text;
 			final_puntos = puntos;
 		} else {
 			texto = "Final score: " + final_puntos;
 		}
		if (Input.GetKeyDown("space")){
			timeLeft = 10000f;
			end = false;
			puntos = 0;
		}
		GUI.Label(new Rect(10, 10, 100, 50), texto);
 	}
}
