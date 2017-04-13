player_schema = {
    "mappings": {
        "player": {
            "properties": {
                "elements": {
                    "type": "object",
                    "properties": {
                        "web_name": {
                            "type": "string"
                        },
                        "team": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "last_name": {
                            "type": "string"
                        },
                        "fantasy_cost_change": {
                            "type": "float"
                        },
                        "in_dreamteam": {
                            "type": "boolean"
                        },
                        "dreamteam_count": {
                            "type": "float"
                        },
                        "selected_percentage": {
                            "type": "float"
                        },
                        "form": {
                            "type": "float"
                        },
                        "fantasy_transfers_out_in": {
                            "type": "float"
                        },
                        "fantasy_total_points": {
                            "type": "float"
                        },
                        "fantasy_points_per_game": {
                            "type": "float"
                        },
                        "minutes_played": {
                            "type": "float"
                        },
                        "goals_scored": {
                            "type": "float"
                        },
                        "assists": {
                            "type": "float"
                        },
                        "yellow_cards": {
                            "type": "float"
                        },
                        "red_cards": {
                            "type": "float"
                        },
                        "bonus" : {
                            "type": "float"
                        },
                        "influence" : {
                            "type": "float"
                        },
                        "creativity" : {
                            "type": "float"
                        },
                        "threat" : {
                            "type": "float"
                        },
                        "ict_index" : {
                            "type": "float"
                        },
                        "ea_index" : {
                            "type": "float"
                        },
                        "icon_link": {
                            "type": "string"
                        }
                    }
                },
                "date_indexed" :{
                    "type" : "date"
                }
            }
        }
    }
}

team_schema = {
    "mappings": {
        "team": {
            "properties": {
                "elements": {
                    "type": "object",
                    "properties": {
                        "team_name": {
                            "type": "string"
                        },
                        "total_shot_ratio": {
                            "type": "float"
                        },
                        "shots_on_target": {
                            "type": "float"
                        },
                        "shoot_percentage": {
                            "type": "float"
                        },
                        "save_percentage": {
                            "type": "float"
                        },
                        "pdo": {
                            "type": "float"
                        }
                    }
                },
                "date_indexed" : {
                        "type" : "date"
                }
            }
        }
    }
}

process_schema = {
    "mappings": {
        "match_data": {
            "properties": {
                "home_team_name": {
                    "type": "string"
                },
                "away_team_name": {
                    "type": "string"
                },
                # all scores and features are home - away and normalized
                "score": {
                    "type": "float"
                },
                "fantasy_cost_change": {
                    "type": "float"
                },
                "in_dreamteam": {
                    "type": "boolean"
                },
                "dreamteam_count": {
                    "type": "float"
                },
                "selected_percentage": {
                    "type": "float"
                },
                "form": {
                    "type": "float"
                },
                "fantasy_transfers_out_in": {
                    "type": "float"
                },
                "fantasy_total_points": {
                    "type": "float"
                },
                "fantasy_points_per_game": {
                    "type": "float"
                },
                "minutes_played": {
                    "type": "float"
                },
                "goals_scored": {
                    "type": "float"
                },
                "assists": {
                    "type": "float"
                },
                "yellow_cards": {
                    "type": "float"
                },
                "red_cards": {
                    "type": "float"
                },
                "bonus": {
                    "type": "float"
                },
                "influence": {
                    "type": "float"
                },
                "creativity": {
                    "type": "float"
                },
                "threat": {
                    "type": "float"
                },
                "ict_index": {
                    "type": "float"
                },
                "ea_index": {
                    "type": "float"
                },
                "total_shot_ratio": {
                    "type": "float"
                },
                "shots_on_target": {
                    "type": "float"
                },
                "shoot_percentage": {
                    "type": "float"
                },
                "save_percentage": {
                    "type": "float"
                },
                "pdo": {
                    "type": "float"
                },
                "date_indexed": {
                    "type": "date"
                }
            }
        }
    }
}
