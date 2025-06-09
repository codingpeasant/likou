import threading
from enum import Enum

class LBMethod(Enum):
    """
    Enumeration of load balancing methods.
    """
    ROUND_ROBIN = "round_robin"
    STICKY = "sticky"

class LoadBalancer:
    """
    A thread-safe load balancer supporting round robin and sticky session strategies.
    """
    def __init__(self, servers):
        """
        Initialize the load balancer with a list of backend servers.

        Args:
            servers (list): A list of server identifiers (e.g., URLs or hostnames).
        """
        if not servers:
            raise ValueError("Server list cannot be empty.")
        self.servers = servers
        self._rr_index = 0
        self._sticky_map = {}
        # Lock to protect concurrent access to rr_index and sticky_map
        self._lock = threading.Lock()

    def get_server_round_robin(self):
        """
        Select the next server using round robin in a thread-safe manner.

        Returns:
            The selected server identifier.
        """
        with self._lock:
            server = self.servers[self._rr_index]
            self._rr_index = (self._rr_index + 1) % len(self.servers)
        return server

    def get_server_sticky(self, client_id):
        """
        Select a server based on sticky session: always route the same client to the same server.
        Thread-safe for concurrent requests.

        Args:
            client_id: A unique identifier for the client (e.g., IP or session cookie).

        Returns:
            The selected server identifier.
        """
        with self._lock:
            if client_id in self._sticky_map:
                return self._sticky_map[client_id]
            # Assign a new server via round robin and record the mapping
            server = self.servers[self._rr_index]
            self._rr_index = (self._rr_index + 1) % len(self.servers)
            self._sticky_map[client_id] = server
        return server

    def get_server(self, client_id=None, method: LBMethod = LBMethod.ROUND_ROBIN):
        """
        Get a backend server for a request.

        Args:
            client_id: Unique client identifier for sticky sessions. Required if method is STICKY.
            method (LBMethod): The load balancing method.

        Returns:
            The selected server identifier.
        """
        if method == LBMethod.STICKY:
            if client_id is None:
                raise ValueError("client_id is required for sticky sessions.")
            return self.get_server_sticky(client_id)
        return self.get_server_round_robin()

if __name__ == "__main__":
    # Example usage demonstrating concurrency safety
    import threading

    backends = [
        "http://backend1.local",
        "http://backend2.local",
        "http://backend3.local"
    ]
    lb = LoadBalancer(backends)

    def make_request(client, method):
        server = lb.get_server(client_id=client, method=method)
        print(f"Request from {client} via {method.value} -> {server}")

    # Simulate concurrent requests
    threads = []
    clients = ["alice", "bob", "charlie", "dave"]
    for client in clients:
        t_rr = threading.Thread(target=make_request, args=(client, LBMethod.ROUND_ROBIN))
        t_st = threading.Thread(target=make_request, args=(client, LBMethod.STICKY))
        threads.extend([t_rr, t_st])

    for t in threads:
        t.start()
    for t in threads:
        t.join()
