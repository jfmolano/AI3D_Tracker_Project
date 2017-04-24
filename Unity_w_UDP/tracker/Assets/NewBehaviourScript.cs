using System.Collections;
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
float yaw;
float pitch;
float roll;

	public static Quaternion ToQ (Vector3 v)
	{
	    return ToQ (v.y, v.x, v.z);
	}

	public static Quaternion ToQ (float yaw, float pitch, float roll)
	{
	    yaw *= Mathf.Deg2Rad;
	    pitch *= Mathf.Deg2Rad;
	    roll *= Mathf.Deg2Rad;
	    float rollOver2 = roll * 0.5f;
	    float sinRollOver2 = (float)Math.Sin ((double)rollOver2);
	    float cosRollOver2 = (float)Math.Cos ((double)rollOver2);
	    float pitchOver2 = pitch * 0.5f;
	    float sinPitchOver2 = (float)Math.Sin ((double)pitchOver2);
	    float cosPitchOver2 = (float)Math.Cos ((double)pitchOver2);
	    float yawOver2 = yaw * 0.5f;
	    float sinYawOver2 = (float)Math.Sin ((double)yawOver2);
	    float cosYawOver2 = (float)Math.Cos ((double)yawOver2);
	    Quaternion result;
	    result.w = cosYawOver2 * cosPitchOver2 * cosRollOver2 + sinYawOver2 * sinPitchOver2 * sinRollOver2;
	    result.x = cosYawOver2 * sinPitchOver2 * cosRollOver2 + sinYawOver2 * cosPitchOver2 * sinRollOver2;
	    result.y = sinYawOver2 * cosPitchOver2 * cosRollOver2 - cosYawOver2 * sinPitchOver2 * sinRollOver2;
	    result.z = cosYawOver2 * cosPitchOver2 * sinRollOver2 - sinYawOver2 * sinPitchOver2 * cosRollOver2;

	    return result;
	}

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
		GameObject.Find("unitychan").transform.rotation = ToQ(yaw, pitch, roll);
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
                yaw = float.Parse(arr_text[2]);
               	pitch = float.Parse(arr_text[3]);
               	roll = float.Parse(arr_text[4]);
            }
            catch (Exception err)
            {
                print(err.ToString());
            }
        }
    }
}
