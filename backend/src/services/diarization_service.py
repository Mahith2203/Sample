async def diarize(path: str, max_speakers: int = 2):
    """
    Implement diarization **without** vendor diarization. Typical approach:
      1. Split audio into speech-active segments
      2. Extract embeddings per segment (pyannote or speechbrain)
      3. Cluster embeddings (k-means with k=max_speakers)
      4. Map clusters back to timestamps and optionally attach text from STT
    Return format example:
    [ {"speaker": "SPEAKER_1", "start": 0.0, "end": 3.2, "text": "..."}, ... ]
    """
    # TODO: implement diarization pipeline
    return [{"speaker": "SPEAKER_1", "start": 0.0, "end": 1.2, "text": "Hello"}, {"speaker": "SPEAKER_2", "start": 1.3, "end": 2.8, "text": "Hi"}]