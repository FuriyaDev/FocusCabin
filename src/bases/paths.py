def user_profile_image_directory_path(instance, filename):
    return f"users/{instance.username}/profile_image/{filename}"