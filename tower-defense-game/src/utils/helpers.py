def load_image(file_path):
    """Load an image from the specified file path."""
    import pygame
    return pygame.image.load(file_path)

def load_sound(file_path):
    """Load a sound from the specified file path."""
    import pygame
    return pygame.mixer.Sound(file_path)

def clamp(value, min_value, max_value):
    """Clamp a value between a minimum and maximum value."""
    return max(min(value, max_value), min_value)

def format_time(seconds):
    """Format time in seconds into a string (MM:SS)."""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def get_random_choice(choices):
    """Return a random choice from a list of choices."""
    import random
    return random.choice(choices)