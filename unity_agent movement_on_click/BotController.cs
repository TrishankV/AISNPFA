using UnityEngine;
using UnityEngine.AI;

public class BotController : MonoBehaviour
{
    public Camera cam;
    public NavMeshAgent agent;

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0)) // Remove the extra parentheses here
        {
            Ray ray = cam.ScreenPointToRay(Input.mousePosition); 
            RaycastHit hit;

            if (Physics.Raycast(ray, out hit)) // if it hits object it will return false
            {
                // move agent
                agent.SetDestination(hit.point);
            }
        }
    }
}
