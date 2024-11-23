import type { MetadataRoute } from "next";
import { getSITEMAPS } from "./actions/getAction";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const Dataa = await getSITEMAPS();

  // Static entries
  const staticEntries: MetadataRoute.Sitemap = [
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
  ];

  // Dynamic entries
  const dynamicEntries: MetadataRoute.Sitemap =
    Dataa?.map((item) => ({
      url: `https://colorhunt.fun/palette/${item.id}`,
      lastModified: item.lastModified || new Date().toISOString(),
      changeFrequency: "weekly",
      priority: 0.5,
      images: [`https://colorhunt.fun/og/${item.id}.png`], // Dynamic image URL
    })) || [];

  // Combine static and dynamic entries
  return [...staticEntries, ...dynamicEntries];
}
