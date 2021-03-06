import sys

import pygame

from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.move_right(True)
    elif event.key == pygame.K_LEFT:
        ship.move_left(True)
    elif event.key == pygame.K_UP:
        ship.move_up(True)
    elif event.key == pygame.K_DOWN:
        ship.move_down(True)
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings=ai_settings,
                    screen=screen, ship=ship, bullets=bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right(False)
    elif event.key == pygame.K_LEFT:
        ship.move_left(False)
    elif event.key == pygame.K_UP:
        ship.move_up(False)
    elif event.key == pygame.K_DOWN:
        ship.move_down(False)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    # Set the background color
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for b in bullets.sprites():
        b.draw_bullet()

    # Make the most recently draw screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if not ai_settings.sideways_shooter:
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        else:
            if bullet.rect.left >= screen.get_rect().right:
                bullets.remove(bullet)


