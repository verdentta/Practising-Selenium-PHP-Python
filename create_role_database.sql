CREATE TABLE user_roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    role_name VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES form_data(id)
);