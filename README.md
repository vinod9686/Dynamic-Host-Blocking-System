# 🛡️ Dynamic Host Blocking System using SDN

## 📖 Introduction

This project demonstrates how **Software Defined Networking (SDN)** can be used to dynamically block network hosts based on their **MAC addresses**. Using the **POX Controller** and **Mininet**, the system centrally manages network security by preventing communication from selected hosts while allowing normal communication for authorized devices.

The project showcases the flexibility of SDN in implementing security policies without manually configuring individual network devices.

---

## 🎯 Objectives

* ✅ Understand SDN architecture and OpenFlow communication.
* ✅ Implement MAC address-based access control.
* ✅ Dynamically block unauthorized hosts.
* ✅ Demonstrate centralized network security management.
* ✅ Simulate network behavior using Mininet.

---

## 🛠️ Technologies Used

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| 🐧 Ubuntu Linux   | Development Environment         |
| 🌐 Mininet        | Network Emulator                |
| 🎮 POX Controller | SDN Controller                  |
| 🔄 OpenFlow       | Controller-Switch Communication |
| 🐍 Python         | Firewall Logic                  |

---

## 🏗️ Network Topology

```text
          +------------------+
          |  POX Controller  |
          | Firewall Module  |
          +--------+---------+
                   |
              OpenFlow
                   |
          +--------+---------+
          | Open vSwitch     |
          +---+----+----+----+
              |    |    |
             h1   h2   h3
```

* 🖥️ **h1** → Source Host
* 🚫 **h2** → Blocked Host
* ✅ **h3** → Allowed Host

---

## ⚙️ How It Works

1. Mininet creates a virtual network.
2. Hosts connect through an OpenFlow switch.
3. POX controller manages the switch.
4. Firewall module checks packet MAC addresses.
5. If the MAC address matches the blocked host:

   * ❌ Packet is dropped.
   * ❌ Communication is denied.
6. Other hosts continue communicating normally.

---

# 🚀 How to Run the Project

## Step 1: Start POX Controller

```bash
cd ~/pox
python3 pox.py openflow.of_01 --port=6633 forwarding.firewall
```

---

## Step 2: Launch Mininet

```bash
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --topo single,3
```

This creates:

* 1 OpenFlow Switch
* 3 Hosts (h1, h2, h3)
* Connection to POX Controller

---

## Step 3: Find Host MAC Address

To check the MAC address of host h2:

```bash
mininet> h2 ifconfig
```

Example:

```text
00:00:00:00:00:02
```

---

## Step 4: Change the MAC Address to Block

Open `firewall.py` and update:

```python
blocked_mac = "00:00:00:00:00:02"
```

👉 Replace the MAC address with the host you want to block in source code.

Examples:

```python
blocked_mac = "00:00:00:00:00:01"  # Block h1
```

```python
blocked_mac = "00:00:00:00:00:02"  # Block h2
```



After changing the MAC address, restart the controller.

---

## 🧪 Testing

### Test Blocked Host

```bash
mininet> h1 ping h2
```

Expected Output:

```text
100% packet loss
```

### Test Allowed Host

```bash
mininet> h1 ping h3
```

Expected Output:

```text
64 bytes from 10.0.0.3
0% packet loss
```

---

## 📊 Results

### 🚫 Blocked Host

```bash
mininet> h1 ping h2

Request timeout
100% packet loss
```

### ✅ Allowed Host

```bash
mininet> h1 ping h3

64 bytes from 10.0.0.3
0% packet loss
```

---

## ✨ Key Features

* 🔒 MAC Address Based Filtering
* ⚡ Dynamic Host Blocking
* 🎯 Centralized Network Control
* 🔄 Real-Time Policy Enforcement
* 🌐 OpenFlow-Based Communication
* 📈 Scalable Security Architecture

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Software Defined Networking (SDN)
* OpenFlow Protocol
* POX Controller Programming
* Mininet Network Emulation
* Network Security Policies
* Firewall Rule Implementation
* MAC Address Filtering

---

## 🔮 Future Enhancements

* 🌐 Web Dashboard for Management
* 🤖 AI-Based Threat Detection
* 📡 Real-Time Traffic Monitoring
* 🔐 IP-Based Filtering
* 🚀 Multiple Host Blocking Support

---

## 🏁 Conclusion

This project successfully demonstrates how **Software Defined Networking (SDN)** can be used to implement centralized network security policies. By combining **POX Controller**, **OpenFlow**, and **Mininet**, the system dynamically blocks hosts based on their MAC addresses while maintaining normal communication for authorized devices.

The project highlights the power of SDN in creating flexible, programmable, and secure network environments.
