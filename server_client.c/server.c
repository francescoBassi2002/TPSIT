#include "includes/utilities.h"
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#define PROMPT "$>"
#define EXIT_CMD "quit"
#define IP_DHCP "0.0.0.0"
#define MAX_STR 1024

void* my_thread(void*);

typedef struct {
	char* msg;
	int sock_id;
	struct sockaddr_in dest;
	pthread_mutex_t mtx;
} Params;


int main(int argc, char* argv[]) {
	if (argc != 3) {
		printf("USAGE: %s PORT MESSAGE\n", argv[0]);
		return -1;
	}

	int port = atoi(argv[1]);
	char* msg = argv[2];

	int socket_id = socket(AF_INET, SOCK_DGRAM, 0);
	if (socket_id == -1) errore("socket()", -2);

	struct sockaddr_in myself;
	myself.sin_family = AF_INET;
	inet_aton(IP_DHCP, &myself.sin_addr);
	myself.sin_port = htons(port);
	for (int i=0; i<8; i++) myself.sin_zero[i] = 0;

	int rc = bind(socket_id,
				(struct sockaddr*) &myself,
				(socklen_t) sizeof(struct sockaddr_in));
	if (rc != 0)
		errore("bind()", -3);


	pthread_t thread_id;
	pthread_mutex_t mutex;
	rc = pthread_mutex_init(&mutex, NULL);
	if (rc != 0) errore("pthread_mutex_init()", -4);

	Params p = {msg, socket_id, myself, mutex};

	rc = pthread_create(&thread_id, NULL, my_thread, (void*) &p);
	if (rc != 0) errore("pthread_create()", -5);

	printf("%s\n", PROMPT);
	char* command = inputStr();
	while(strcmp(command, EXIT_CMD)) {
		free(command);
		printf("%s\n", PROMPT);
		command = inputStr();
	}
	free(command);

	close(socket_id);

	return 0;	
}


void* my_thread(void* param) {
	Params* p = (Params*) param;

	struct sockaddr_in dest;
	int addr_len = sizeof(struct sockaddr);
	char buffer[MAX_STR + 1];
	int rc = recvfrom(p->sock_id, 
						buffer, 
						MAX_STR, 
						0, 
						(struct sockaddr*)&dest, 
						(socklen_t*)&addr_len);
	if (rc <= 0) errore("recvfrom()", -6);

	pthread_mutex_lock(&p->mtx);
	char* ip = strdup(inet_ntoa(dest.sin_addr));
	pthread_mutex_unlock(&p->mtx);
	int port = ntohs(dest.sin_port);	
	buffer[rc] = '\0';

	printf("%s received from [%s:%d] '%s'\n", PROMPT, ip, port, buffer);

	rc = sendto(p->sock_id,
				p->msg,
				strlen(p->msg)+1,
				0,
				(struct sockaddr*) &dest,
				(socklen_t) sizeof(struct sockaddr_in));
	if (rc != strlen(p->msg)+1)
		errore("sendto()", -7);
	printf("%s sent to [%s:%d] '%s'\n", PROMPT, ip, port, p->msg);
	
	return NULL;
}