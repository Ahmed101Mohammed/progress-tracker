data_structure = [
                    {
                        "table_title": "users",
                        "table_columons": [ "id INTEGER PRIMARY KEY AUTOINCREMENT",
                                            "name TEXT UNIQUE",
                                            "hours REAL"
                                            ]
                    }
                    ,{
                        "table_title": "subjects",
                        "table_columons": [ "id INTEGER PRIMARY KEY AUTOINCREMENT",
                                            "title TEXT UNIQUE"
                                            ]
                    }
                    ,{
                        "table_title": "goals",
                        "table_columons": [ "id INTEGER PRIMARY KEY AUTOINCREMENT",
                                            "user_id INTEGER",
                                            "subject_id INTEGER",
                                            "target_hours REAL",
                                            "progress REAL"
                                            ]
                    }
                    ,{
                        "table_title": "commits",
                        "table_columons": [ "id INTEGER PRIMARY KEY AUTOINCREMENT",
                                            "goal_id INTEGER",
                                            "hours REAL",
                                            "comment TEXT",
                                            ]
                    }
                ]