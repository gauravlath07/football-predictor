schema = {
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
                            "type": "integer"
                        },
                        "in_dreamteam": {
                            "type": "boolean"
                        },
                        "dreamteam_count": {
                            "type": "integer"
                        },
                        "selected_percentage": {
                            "type": "integer"
                        },
                        "form": {
                            "type": "integer"
                        },
                        "fantasy_transfers_in": {
                            "type": "integer"
                        },
                        "fantasy_transfers_out": {
                            "type": "integer"
                        },
                        "fantasy_total_points": {
                            "type": "integer"
                        },
                        "fantasy_points_per_game": {
                            "type": "integer"
                        },
                        "minutes_played": {
                            "type": "integer"
                        },
                        "goals_scored": {
                            "type": "integer"
                        },
                        "assists": {
                            "type": "integer"
                        },
                        "yellow_cards": {
                            "type": "integer"
                        },
                        "red_cards": {
                            "type": "integer"
                        },
                        "bonus" : {
                            "type": "integer"
                        },
                        "influence" : {
                            "type": "integer"
                        },
                        "creativity" : {
                            "type": "integer"
                        },
                        "threat" : {
                            "type": "integer"
                        },
                        "ict_index" : {
                            "type": "integer"
                        },
                        "ea_index" : {
                            "type": "integer"
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