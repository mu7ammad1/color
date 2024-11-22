import type { MetadataRoute } from "next";

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: "https://colorhunt.fun",
      lastModified: "2021-01-01",
      changeFrequency: "weekly",
      priority: 0.5,
      images: ["https://example.com/image.jpg"],
    },
    {
      url: "https://colorhunt.fun/palette/83580bd9b650f5dd7bfde994",
      lastModified: "2021-01-01",
      changeFrequency: "weekly",
      priority: 0.5,
      images: ["https://example.com/83580bd9b650f5dd7bfde994.jpg"],
    },
    {
      url: "https://colorhunt.fun",
      lastModified: "2021-01-01",
      changeFrequency: "weekly",
      priority: 0.5,
      images: ["https://example.com/image.jpg"],
    },
  ];
}
