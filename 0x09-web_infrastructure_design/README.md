# Scalable Web Infrastructure Project

This project aims to design a scalable web infrastructure capable of handling increased traffic and maintaining high availability. The infrastructure includes load balancers, web servers, application servers, and database servers, distributed across multiple servers to ensure redundancy and scalability.

## Project Components

### Load Balancer Cluster (HAproxy)

The infrastructure includes a load balancer cluster consisting of two HAproxy instances. These load balancers distribute incoming traffic efficiently among multiple web and application servers, enhancing scalability and fault tolerance.

### Web Servers

Two instances of Nginx web servers are deployed behind the load balancer cluster. These servers handle incoming HTTP requests and serve static content to users.

### Application Servers

Two application servers are deployed to host the application logic and handle dynamic content generation. These servers ensure redundancy and scalability for the application layer.

### Database Servers

Two MySQL database servers are deployed to store and manage the website's data. These servers are configured in a cluster to provide fault tolerance and scalability for data storage.

## Additional Elements

### Why Are Additional Elements Added?

- **Load Balancer Cluster**: Added to evenly distribute incoming traffic and ensure high availability.
- **Split Components with Their Own Servers**: Separating components onto dedicated servers allows for better resource utilization, scalability, and fault isolation.

## Issues and Considerations

### Potential Issues

- **Terminating SSL at Load Balancer Level**: Terminating SSL at the load balancer may expose decrypted traffic within the internal network, potentially compromising data security.
- **Single MySQL Server Accepting Writes**: Having only one MySQL server capable of accepting writes poses a single point of failure and potential performance bottlenecks.
- **Uniform Server Components**: Having servers with identical components may lead to uniform failure points and scalability limitations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.