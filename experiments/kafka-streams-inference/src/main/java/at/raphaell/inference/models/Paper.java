package at.raphaell.inference.models;

import com.fasterxml.jackson.annotation.JsonProperty;

public record Paper(
        @JsonProperty("title") String title,
        @JsonProperty("abstract") String abstract_,
        @JsonProperty("doi") String doi
) {}
