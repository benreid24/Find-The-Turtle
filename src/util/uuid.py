import pygame

CURRENT_EVENT_ID = pygame.USEREVENT + 1
CURRENT_UUID = 1


def get_unique_event_id():
    global CURRENT_EVENT_ID
    ret_id = CURRENT_EVENT_ID
    CURRENT_EVENT_ID += 1
    return ret_id


def get_next_uuid():
    global CURRENT_UUID
    ret_id = CURRENT_UUID + 1
    CURRENT_UUID += 1
    return ret_id
