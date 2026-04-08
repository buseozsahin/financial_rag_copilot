def get_rag_config(mode):
    configs = {
        "fast": {
            "top_k": 4,
            "max_chunks": 2,
            "max_tokens": 150,
            "style": "concise and direct"
        },
        "balanced": {
            "top_k": 6,
            "max_chunks": 4,
            "max_tokens": 300,
            "style": "clear and structured"
        },
        "accurate": {
            "top_k": 10,
            "max_chunks": 8,
            "max_tokens": 600,
            "style": "detailed and comprehensive"
        }
    }

    return configs.get(mode, configs["balanced"])