o
    I��e�  �                   @   s&   d dl mZmZ G dd� dej�ZdS )�    )�
migrations�modelsc                   @   s�   e Zd ZdgZejddejddddd�fdejd	d
�fdejd	d
�fgd�ej	dddd�ej
ddd�ejddejdd�d�ejddejddd�dd�ejddejdd�d�gZdS )�	Migration)�main_app�0003_auto_20240122_1521�
Ingredient�idTF�ID)�auto_created�primary_key�	serialize�verbose_name�name��   )�
max_length�	image_url)r   �fields�shoppinglist�ingredient_name�
drinkImage)�
model_name�old_name�new_name�ingredient_id)r   r   �drinkInstructions� )�default)r   r   �field�idDrink�   )r   r   )r   r   r   �preserve_default�ingredientszmain_app.Ingredient)�toN)�__name__�
__module__�__qualname__�dependenciesr   �CreateModelr   �BigAutoField�	CharField�RenameField�RemoveField�AddField�	TextField�ManyToManyField�
operations� r0   r0   �i/home/irishjack/sei/projects/Project3/DrinksApp/Drinks-app/main_app/migrations/0004_auto_20240122_1631.pyr      sH    �����
��
��r   N)�	django.dbr   r   r   r0   r0   r0   r1   �<module>   s   