import pygame

CURRENT_EVENT_ID = pygame.USEREVENT + 1


def get_unique_event_id():
    global CURRENT_EVENT_ID
    ret_id = CURRENT_EVENT_ID
    CURRENT_EVENT_ID += 1
    return ret_id
