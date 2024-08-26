SELECT  form_data.name, form_data.email, user_roles.role_name
FROM form_data
INNER JOIN user_roles ON form_data.id = user_roles.user_id