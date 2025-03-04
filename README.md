# Real-Time Fraud Detection

## Overview
This project implements a **real-time fraud detection pipeline**  using a robust tech stack icluding **Apache Airflow**, **Python**, **Apache Kafka**, **Apache Zookeeper**, **Apache Spark**, and **Cassandra**. Everything is containerized using **Docker** for ease of deployment and scalability.
It processes incoming transactions in real-time, applies rule-based detection, and triggers automated workflows using **Airflow**.

## Architecture
The application consists of the following components:

- **Kafka**: Handles real-time transaction streaming.
- **Spark Streaming**: Processes data streams and applies fraud detection rules.
- **Cassandra**: Stores processed transactions for analysis and reporting.
- **Airflow**: Automates workflows for fraud alerts and data management.
- **Docker**: Manages containerized deployment for scalability and portability.


## Setup
### Prerequisites
Ensure you have the following installed:
- Docker & Docker Compose
- Python 3.9
- Java 11
- Hadoop & winutils (For Windows users only)
- Apache Kafka(Dockerized)
- Apache Spark(Dockerized)
- Apache Airflow(Dockerized)
- Cassandra(Dockerized)


### Setting up Hadoop and `winutils.exe` (Windows Only)
Spark requires `winutils.exe` and Hadoop binaries on Windows. Follow these steps:

1. **Download winutils.exe and Hadoop binaries:**
   - Download the correct **winutils.exe and hadoop,dll** version for your Spark installation this application uses version 3.3.5    from [winutils repository](https://github.com/cdarlint/winutils).

2. **Move winutils.exe and hadoop.dll:**
   - Place `winutils.exe` and `hadoop.dll`inside `C:\hadoop\bin`.
   - Add a copy of `hadoop.dll` inside `C:\Windows\System32`

4. **Set Environment Variables:**
   - Open **System Properties** → **Advanced** → **Environment Variables**.
   - Add a new system variable:
     ```plaintext
     HADOOP_HOME = C:\hadoop
     ```
   - Edit the `Path` variable and add:
     ```plaintext
     C:\hadoop\bin
     ```

5. **Verify Installation:**
   - Open **Command Prompt** and run:
     ```sh
     winutils.exe ls C:\hadoop\bin
     ```
   - If no errors appear, Hadoop and winutils are set up correctly.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/realtime-fraud-detection.git
   cd realtime-fraud-detection
2. Start the services using Docker:
   ```bash
   docker-compose up -d


## Future Requirements
- **Machine Learning Integration**: Implement anomaly detection models to enhance fraud detection accuracy.
- **Real-Time Alerting System**: Integrate with notification services such as Slack, email, or SMS.
- **Scalability Enhancements**: Optimize for high-throughput environments with auto-scaling.
- **Data Visualization**: Implement dashboards using Grafana or Apache Superset for real-time monitoring.
- **Multi-Cloud Deployment**: Adapt the system to work seamlessly across AWS, GCP, and Azure.

## Contributing
Contributions are welcome! Feel free to submit pull requests or open issues.

## License
This project is licensed under the **MIT License**. 