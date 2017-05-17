using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class r_4 : MonoBehaviour {

GameObject r;
float rand;

	// Use this for initialization
	void Start () {
		r = GameObject.Find("Strawberry");
		rand = 0.05f;
	}
	
	// Update is called once per frame
	void Update () {
		r.transform.position += new Vector3(0f, 0f, rand);
		if(r.transform.position.z > 12f){
		    float rand_x = Random.Range(0.3f, 7.5f);
		    float rand_y = Random.Range(2.9f, 6.0f);
			r.transform.position = new Vector3(rand_x, rand_y, -5f);
			rand = Random.Range(0.2f, 0.3f);
			print("BACK 1");
			print(rand);
		}
	}

    void OnCollisionEnter(Collision collisionInfo)
	{
	    print("Colision");
	    float rand_x = Random.Range(0.3f, 7.5f);
	    float rand_y = Random.Range(2.9f, 6.0f);
		r.transform.position = new Vector3(rand_x, rand_y, -10f);
		Score.puntos += 20;
	}

}
