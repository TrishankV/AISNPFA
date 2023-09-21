using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;
using UnityEngine.AI;

public class BotController : MonoBehaviour
{

    public NavMeshAgent agent;
    private Thread mThread; // Declare the Thread object
    private IPAddress localAdd;
    private TcpListener listener;
    private TcpClient client;
    private bool running = false;
    private Vector3 receivedPos;
    private string connectionIP = "127.0.0.1"; // Change to the appropriate IP address
    private int connectionPort = 25001;

    // Update is called once per frame
    void Update()
    {
        // if (Input.GetMouseButtonDown(0)) // Remove the extra parentheses here
        // {
        //     Ray ray = cam.ScreenPointToRay(Input.mousePosition);
        //     RaycastHit hit;

        //     if (Physics.Raycast(ray, out hit)) // if it hits object it will return false
        //     {
        //         // move agent
        //         agent.SetDestination(hit.point);
        //     }
        // }
        if (receivedPos != Vector3.zero)
        {
            agent.SetDestination(receivedPos);
        }
    }

    // Added Code
        private void Start()
    {
        ThreadStart ts = new ThreadStart(GetInfo);
        mThread = new Thread(ts);
        mThread.Start();

    }

    void GetInfo()
    {
        localAdd = IPAddress.Parse(connectionIP);
        listener = new TcpListener(IPAddress.Any, connectionPort);
        listener.Start();

        client = listener.AcceptTcpClient();

        running = true;
        while (running)
        {
            SendAndReceiveData();
        }
        listener.Stop();
    }

    void SendAndReceiveData()
    {
        NetworkStream nwStream = client.GetStream();
        byte[] buffer = new byte[client.ReceiveBufferSize];

        //---receiving Data from the Host----
        int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize); //Getting data in Bytes from Python
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead); //Converting byte data to string

        if (dataReceived != null)
        {
            //---Using received data---
            receivedPos = StringToVector3(dataReceived); //<-- assigning receivedPos value from Python
            print("received pos data, and moved the Cube!");

            //---Sending Data to Host----
            byte[] myWriteBuffer = Encoding.ASCII.GetBytes("Hey I got your message Python! Do You see this massage?"); //Converting string to byte data
            nwStream.Write(myWriteBuffer, 0, myWriteBuffer.Length); //Sending the data in Bytes to Python
        }
    }

    public static Vector3 StringToVector3(string sVector)
    {
        // Remove the parentheses
        if (sVector.StartsWith("(") && sVector.EndsWith(")"))
        {
            sVector = sVector.Substring(1, sVector.Length - 2);
        }

        // split the items
        string[] sArray = sVector.Split(',');

        // store as a Vector3
        Vector3 result = new Vector3(
            float.Parse(sArray[0]),
            float.Parse(sArray[1]),
            float.Parse(sArray[2]));

        return result;
    }
}