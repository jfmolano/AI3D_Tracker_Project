﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Threading;

public class NewBehaviourScript : MonoBehaviour {
GameObject sphere;
UdpClient client;
Thread receiveThread;
float x;
float y;
float z;
	// Use this for initialization
	void Start () {
		//sphere = new GameObject.Find("/Sphere");
		receiveThread = new Thread(
            new ThreadStart(ReceiveData));
        receiveThread.IsBackground = true;
        receiveThread.Start();
        print("Start");
        y = 0;
        z = 0;
	}
	
	// Update is called once per frame
	void Update () {
		GameObject.Find("unitychan").transform.position = new Vector3(x, y, z);
		//GameObject.Find("Sphere/Texto").GetComponent<TextMesh>().text = "" + x;
	}

	private void ReceiveData()
    {
    	int port = 8080;
        client = new UdpClient(port);
        while (true)
        {
 
            try
            {
            	print("On thread");
                // Bytes empfangen.
                IPEndPoint anyIP = new IPEndPoint(IPAddress.Any, 0);
                print("IPEndPoint");
                byte[] data = client.Receive(ref anyIP);
 				print("data");
                // Bytes mit der UTF8-Kodierung in das Textformat kodieren.
                string text = Encoding.UTF8.GetString(data);
                string[] arr_text = text.Split(new string[] { ";" }, StringSplitOptions.None);
 				print("text " + arr_text[0] + " " + arr_text[1]);
                x = float.Parse(arr_text[0]);
               	y = float.Parse(arr_text[1]);
            }
            catch (Exception err)
            {
                print(err.ToString());
            }
        }
    }
}
