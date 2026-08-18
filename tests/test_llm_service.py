from app.infrastruture.llm.llm_service import OllamaLLMService


def test_ollama_llm_service():  
    llm_service=OllamaLLMService()

    prompt="what is rag give in 1 line"

    ans=llm_service.generate(prompt)

    print("\nLLM Answer")

    assert isinstance(ans, str)

    assert len(ans) > 0


    

