schema = {
    "mappings": {
        "player": {
            "properties": {
                "name": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "total_points": {
                    "type": "integer",
                    "index": "not_analyzed"
                },
                "goals": {
                    "type": "string"
                },
                "assists": {
                    "type": "string"
                },

                "minutes_played": {
                    "type": "date"
                },
                "current_form": {
                    "type": "string"
                },
                "ea_index": {
                    "type": "string"
                },
                "status": {
                    "type": "string"
                },
                "news": {
                    "type": "string"
                }
            }
        }
    }
}