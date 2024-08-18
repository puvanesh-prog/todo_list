

-- Create the tasks table
CREATE TABLE tasks (
  id INT AUTO_INCREMENT,
  task VARCHAR(255) NOT NULL,
  PRIMARY KEY (id));


Insert into tasks (task) values('brush');



SELECT * FROM tasks;