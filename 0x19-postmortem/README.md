### Postmortem: Outage Incident on Web Application

![image](img.jpg)

**Issue Summary:**
- **Duration:** June 19, 2024, 7:00 AM — June 20, 2024, 2:00 AM (UTC)
- **Impact:** The web application experienced intermittent downtime, resulting in slow response times and partial service disruption. Approximately 20% of users were affected during this period.
- **Root Cause:** Overloaded cache layer leading to increased latency and intermittent failures.

**Timeline:**
- **June 19, 2024, 7:15 AM (UTC):** Issue detected via monitoring alerts indicating a significant increase in response time.
- **7:30 AM:** Engineering team began investigating, suspecting a database problem due to recent schema changes.
- **8:00 AM:** Investigation focused on database cluster; no issues found.
- **9:00 AM:** Incident escalated to database administration team.
- **June 20, 2024, 10:30 PM (UTC):** Root cause identified as an overloaded cache layer.
- **1:00 AM:** Incident escalated to infrastructure team for resolution.
- **2:00 AM:** Issue resolved; web application performance returned to normal.

**Root Cause and Resolution:**
- **Root Cause:** The cache layer was overloaded, causing frequent eviction of accessed data, resulting in high latency and intermittent failures. The eviction policy was not configured to handle the traffic surge.
- **Resolution:** The infrastructure team increased the cache capacity and optimized the eviction policy. A monitoring system was implemented to provide early warnings when cache utilization reaches critical levels.

**Corrective and Preventative Measures:**
- **Optimize Cache Eviction Policies:** Review and fine-tune eviction policies based on usage patterns and traffic fluctuations.
- **Scale Cache Infrastructure:** Evaluate and scale cache infrastructure as needed, potentially introducing distributed caching solutions.
- **Enhance Monitoring and Alerts:** Implement comprehensive monitoring for cache utilization, response times, and database performance to promptly identify anomalies.
- **Load Testing and Capacity Planning:** Regularly perform load testing to simulate various traffic scenarios, ensuring the system can handle peak loads without performance degradation.
- **Improve Incident Response Process:** Refine escalation paths and clearly define roles and responsibilities for incident response, ensuring efficient team collaboration during critical situations.

**Tasks to Address the Issue:**
- **Patch Cache Eviction Policies:** Adjust policies to prioritize frequently accessed data while considering memory constraints.
- **Evaluate Cache Infrastructure:** Assess current capacity and explore scaling or distributed caching options.
- **Implement Comprehensive Monitoring:** Deploy a solution covering cache utilization, response times, and database performance with appropriate alerts.
- **Conduct Load Testing:** Develop and execute scenarios to validate system performance under varying traffic conditions.
- **Review and Update Incident Response Procedures:** Enhance the process for swift identification, investigation, and resolution of future incidents.
