

INSERT INTO
    IS601_Roles (
        id,
        name,
        description,
        is_active
    )
VALUES (-2, 'Admin2', 'Secondary Admin', 1) ON DUPLICATE KEY
UPDATE name = name;