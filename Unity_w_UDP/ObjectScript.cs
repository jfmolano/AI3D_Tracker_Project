using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour {
GameObject sphere;
	// Use this for initialization
	void Start () {
		//sphere = new GameObject.Find("/Sphere");
	}
	
	// Update is called once per frame
	void Update () {
		GameObject.Find("Sphere").transform.position = new Vector3(1, 1, 1);
	}
}
