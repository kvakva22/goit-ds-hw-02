SELECT * FROM tasks WHERE user_id = 2;

SELECT * FROM tasks WHERE status_id = 1;

UPDATE tasks 
SET status_id = 2 WHERE status_id = 1;

SELECT * FROM users 
WHERE id NOT IN (
	SELECT user_id FROM tasks);

INSERT INTO tasks(id, title, description, status_id, user_id)
VALUES(21, 'Do some chores', "Wash dishes, clean the house etc", "1", "2");

SELECT * FROM tasks WHERE status_id != 3;

DELETE FROM tasks WHERE id = 15;

SELECT * FROM users WHERE email LIKE '%example.org';

UPDATE users 
SET fullname = 'Vasily Pablo' WHERE id = 1;

SELECT COUNT(*) FROM tasks WHERE status_id IN (1, 2, 3)
GROUP BY status_id;

SELECT tasks.*, users.fullname, users.email FROM tasks 
JOIN users ON users.id = tasks.user_id 
WHERE users.email LIKE '%@example.com';


SELECT * FROM tasks 
WHERE description IS NULL;

SELECT tasks.*, users.fullname FROM tasks
INNER JOIN users ON users.id = tasks.user_id 
WHERE tasks.status_id = 2;

SELECT COUNT(*), users.fullname FROM tasks
LEFT JOIN users on users.id = tasks.user_id 
GROUP BY users.id;